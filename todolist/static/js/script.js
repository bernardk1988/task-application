//delete
document.querySelectorAll(".deleteForm").forEach(form => {
    form.addEventListener("submit", function(event) {
        event.preventDefault();
        if (!confirm("Are you sure you want to delete this task?")) {
            return;
        }
        fetch(form.action, {
            method: "POST",
            body: new FormData(form)
        })
        .then(response => response.json())
        .then(data => {
            console.log("DRF Response:", data);
            alert(data.message);
            if (data.success) {
                window.location.href = "/";
            }
        })
        .catch(error => {
            console.error("Error:", error);
            alert("Delete failed!");
        });
    });
});

//add and update
const todoForm = document.getElementById("todoForm");
todoForm.addEventListener("submit", function(event) {
    event.preventDefault();
    console.log("API URL:", todoForm.action);
    fetch(todoForm.action, {
        method: "POST",
        body: new FormData(todoForm)
    })
    .then(async response => {
        const result = await response.text();
        console.log("Status:", response.status);
        console.log("Content Type:", response.headers.get("content-type"));
        console.log("Response:", result);
        if (!response.headers.get("content-type")?.includes("application/json")) {
            throw new Error("Django returned HTML instead of JSON. Check Console.");
        }
        return JSON.parse(result);
    })
    .then(data => {

        alert(data.message);

        if (data.success) {
            window.location.href = "/";
        }
    })
    .catch(error => {
        console.error(error);
        alert(error.message);
    });
});

