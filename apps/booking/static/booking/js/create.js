const checkin = document.getElementById("id_check_in");
const checkout = document.getElementById("id_check_out");
const numberOfGuests = document.getElementById("id_number_of_guests")
const totalPrice = document.getElementById('total-price');
const bookingForm = document.getElementById('booking-create-form');
const serviceCheckboxes = document.querySelectorAll(
    'input[name="services"]'
);

const today = new Date();
const todayStr = today.toISOString().split("T")[0];
checkin.min = todayStr;

checkin.addEventListener("change", () => {
  const next = new Date(checkin.value);
  next.setDate(next.getDate() + 1);
  checkout.min = next.toISOString().split("T")[0];

  if (checkout.value && checkout.value < checkout.min) {
    checkout.value = checkout.min;
  }
});

async function updatePrice() {
    const selectedServices = Array.from(serviceCheckboxes)
        .filter(checkbox => checkbox.checked)
        .map(checkbox => checkbox.value);

    const csrfToken = bookingForm.querySelector(
        '[name="csrfmiddlewaretoken"]'
    ).value;
    const response = await fetch(bookingForm.dataset.priceUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({
            check_in: checkin.value,
            check_out: checkout.value,
            number_of_guests: numberOfGuests.value,
            services: selectedServices
        })
    });

    if (!response.ok) {
        throw new Error(`Price update failed: ${response.status}`);
    }
    const data = await response.json();
    totalPrice.textContent = `${data.price} ₴`;
}

checkin.addEventListener('change', updatePrice);
checkout.addEventListener('change', updatePrice);
numberOfGuests.addEventListener('change', updatePrice);

serviceCheckboxes.forEach(checkbox => {
    checkbox.addEventListener('change', updatePrice);
});

updatePrice();
