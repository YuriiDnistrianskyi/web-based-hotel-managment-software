dateOfBidth = document.getElementById("id_date_of_birth");

const today = new Date().toISOString().split("T")[0];
dateOfBidth.max = today;
