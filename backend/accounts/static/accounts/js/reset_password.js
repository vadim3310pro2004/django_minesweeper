
const validatePassword = (password, confirmPassword) => {
    const errors = [];

    if (!/^[a-zA-Z0-9]+$/g.test(password)) 
        errors.push("Only english letters and numbers allowed");
    if (!/(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])/.test(password))
        errors.push("Password must includes numbers, uppercase and lowercase letters");
    if (password.length < 8)
        errors.push("Min length of password 8 chars");
    if (password.length > 32)
        errors.push("Max length of password 32 chars");
    if (confirmPassword !== password)
        errors.push("Confirm password must be equal password");

    if (errors.length === 0) {
        return;
    }
    return errors;
}

const sendTo = JSON.parse(document.getElementById('send-to').textContent);
const [uid, token] = window.location.href.split("/").slice(-2);
const openErrors = document.querySelector("#openErrorsModal");
const errorsContainer = document.querySelector("#errors");
const form = document.querySelector("form")
const [password, confirmPassword] = form.querySelectorAll("input[type=password]");



form.onsubmit = (event) => {
    event.preventDefault();
    const errors = validatePassword(password.value, confirmPassword.value);
    
    if (errors) {
        errorsContainer.innerHTML = errors.reduce((prew, item) => (
            prew + "<br>" + item
        ));
        openErrors.click();
    }
    else {
        const requestOptions = {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                uid,
                token,
                new_password: password.value,
                re_new_password: confirmPassword.value,
            }),  
        };

        fetch(sendTo, requestOptions).then(response => {
            if (!response.ok) {
                throw new Error(response.statusText);
            }
            else {
                return response.text();
            }
        }).then(() => {
            document.body.innerHTML = `
                <div class="text-center text-success fs-2 fw-bold">
                    Success !
                </div>
            `
        }).catch(error => {
            document.body.innerHTML = `
                <div class="text-center text-danger fs-2 fw-bold">
                    Error
                </div>
            `;
        });
    }
};
