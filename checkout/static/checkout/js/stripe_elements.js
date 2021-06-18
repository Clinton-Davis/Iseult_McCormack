/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
*/
let stripePublicKey = document.querySelector("#id_stripe_public_key").innerHTML.slice(1, -1);

let clientSecret = document.querySelector("#id_client_secret").innerHTML.slice(1, -1);
// var country = $("#id_country").text().slice(1, -1);
let stripe = Stripe(stripePublicKey);
let elements = stripe.elements();

var card = elements.create("card");
card.mount("#card-element");

// Handle realtime validation errors on the card element
card.addEventListener("change",  (event) => {
  let errorDisplay = document.querySelector("#card-errors");
  if (event.error) {
    let html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
    errorDisplay.innerHTML = html;
  } else {
    errorDisplay.textContent = "";
  }
});

// Handle form submit
let form = document.getElementById("payment-form");

form.addEventListener("submit", (ev) => {
  ev.preventDefault();

  card.update({
    disabled: true,
  });

  document.querySelector("#submit-button").setAttribute("disabled", true);
  document.querySelector(".loading-overlay").classList.add("loading-spinner");
  // $("#payment-form").fadeToggle(100);
  // $("#loading-overlay").fadeToggle(100);

  let saveButton = document.querySelector("#save-info");
  let saveInfo = false;
  if (saveButton) {
      saveInfo = Boolean(saveButton.hasAttribute("checked"));
  }

  // From using {% csrf_token %} in the form
  let csrfToken = document.querySelector('[name="csrfmiddlewaretoken"]').value;
  let postData = new FormData();
   postData.set("csrfmiddlewaretoken", csrfToken);
    postData.set("client_secret", clientSecret);
    postData.set("save_info", saveInfo);
    let url = "/checkout/cache_checkout_data/";

    fetch(url, {
      method: "POST",
      headers: {
          "X-CSRFToken": csrfToken,
      },
      body: postData

    }).then(() => {
          stripe.confirmCardPayment(clientSecret, {
          payment_method: {
            card: card,
            billing_details: {
              email: $.trim(form.email.value),
            },
          },
        })
        .then((result) => {
          let errorDisplay = document.querySelector("#card-errors");
          if (result.error) {
            let html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-exclamation-triangle"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                    errorDisplay.innerHTML = html;
                    document.querySelector(".loading").classList.remove("loading-show");
            
            card.update({
              disabled: false,
            });
            document.querySelector("#submit-button").removeAttribute("disabled");
          } else {
            if (result.paymentIntent.status === "succeeded") {
              form.submit();
            }
          }
        });
    }).catch((error) => {
     
      location.reload();
    });
   
      
});

