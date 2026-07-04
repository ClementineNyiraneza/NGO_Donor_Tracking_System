document.addEventListener("DOMContentLoaded", function () {
    const forms = document.querySelectorAll("form");

    forms.forEach(function (form) {
        form.addEventListener("submit", function (event) {
            const inputs = form.querySelectorAll("input, textarea, select");
            let valid = true;

            inputs.forEach(function (input) {
                if (input.hasAttribute("required") && input.value.trim() === "") {
                    valid = false;
                    input.classList.add("is-invalid");
                } else {
                    input.classList.remove("is-invalid");
                }
            });

            if (!valid) {
                event.preventDefault();
                alert("Please fill in all required fields before submitting.");
            }
        });
    });
});