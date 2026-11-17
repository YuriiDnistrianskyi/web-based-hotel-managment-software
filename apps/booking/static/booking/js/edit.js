const checkin = document.getElementById("id_check_in");
const checkout = document.getElementById("id_check_out");
const numberOfGuests = document.getElementById("id_number_of_guests")
const totalPrice = document.getElementById('total-price');
const bookingForm = document.getElementById('booking-edit-form');
const serviceCheckboxes = document.querySelectorAll(
    'input[name="services"]'
);

const today = new Date()

const tomorrow = new Date()
tomorrow.setDate(today.getDate() + 1)

const todayStr = today.toISOString().split("T")[0];
const tomorrowStr = tomorrow.toISOString().split("T")[0];

const isStart = bookingForm.dataset.status == 'Confirmed' ? false : true;

if (isStart) {
    checkin.readOnly = true;
    checkout.min = todayStr;
} else {
    checkin.min = todayStr;
    checkout.min = tomorrowStr;
}

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
