

const sendTo = JSON.parse(document.getElementById('send-to').textContent);
const [uid, token] = window.location.href.split('/').slice(-2);
const statusElement = document.querySelector('.status');

const requestOptions = {
    method: 'POST',
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        uid,
        token,
    }),
};

fetch(sendTo, requestOptions)
    .then(response => { 
        if (!response.ok) {
            throw new Error(response.statusText)
        } 
        else {
            return response.text();
        }
    })
    .then(result => {
        statusElement.innerHTML = 'Success';
        statusElement.classList.add("text-success");
        statusElement.classList.remove("text-danger");
        statusElement.classList.remove("text-light");
        console.log(result);
    })
    .catch(error => {
        statusElement.innerHTML = 'Error';
        statusElement.classList.add("text-danger");
        statusElement.classList.remove("text-success");
        statusElement.classList.remove("text-light");
        return console.log("error", error);
    });

