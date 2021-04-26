var bookedSeats = [];
var countOfPerson = 0;
// get show id
var showId = window.location.href.slice(27);
var selectSeats = document.getElementById("selectSeats");
var seatsToBeBooked = [];
// get booked seats
$(document).ready(() => {
var allowBook = document.getElementById("allowBook");
  allowBook.style.display = "none";
  $.ajax({
    type: "GET",
    data: {},
    url: window.location.origin + `/show/${showId}/getBookings`,
    success: function (value) {
      bookedSeats = value.bookedSeats;
      renderSeats();
    },
  });
});

function renderSeats() {
  for (num of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) {
    if (bookedSeats.indexOf(num) == -1) {
      selectSeats.innerHTML += `<div class="form-check form-check-inline">
            <input onchange="updateSeatCount()" class="form-check-input" type="checkbox" id="inlineCheckbox${num}" value="option${num}">
            <label class="form-check-label" for="inlineCheckbox${num}">${num}</label>
          </div>`;
    } else {
      selectSeats.innerHTML += `<div class="form-check form-check-inline">
            <input onchange="updateSeatCount()" class="form-check-input" type="checkbox" id="inlineCheckbox${num}" value="option${num}" disabled>
            <label class="form-check-label" for="inlineCheckbox${num}">${num}</label>
          </div>`;
    }
  }
}

function updateSeatCount() {
  all_seats = document.querySelectorAll("#selectSeats input[type=checkbox]");
  countOfPerson = 0;
  seatsToBeBooked = [];
  let i = 0;
  for (num of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) {
    if (all_seats[num - 1].checked) {
      countOfPerson++;
      seatsToBeBooked[i++] = num;
    }
  }
  if (countOfPerson == 0) {
    allowBook.style.display = "none";
  } else {
    allowBook.style.display = "block";
  }
  document.getElementById("noOfPerson").innerText = countOfPerson;
  document.getElementById("amount").innerText =
    "₹" + ticketPrice * countOfPerson;
}

function bookTickets() {
  console.log(seatsToBeBooked);
  $.ajax({
    type: "POST",
    data: {
      csrfmiddlewaretoken: getCSRFToken(),
      "seatsBooked[]": seatsToBeBooked,
      noOfPerson: countOfPerson,
      total: ticketPrice * countOfPerson,
    },
    url: window.location.origin + `/show/${showId}/bookSeats`,
    success: function (value) {
      console.log(value);
      if (value.status) {
        window.location.href = "../../success";
      }
    },
  });
}

// CSRF TOKEN

function getCSRFToken() {
  var cookieValue = null;
  if (document.cookie && document.cookie != "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      if (cookie.substring(0, 10) == "csrftoken" + "=") {
        cookieValue = decodeURIComponent(cookie.substring(10));
        break;
      }
    }
  }
  return cookieValue;
}
