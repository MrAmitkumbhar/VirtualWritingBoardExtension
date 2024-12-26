document.getElementById("launch").addEventListener("click", async () => {
    try {
        const response = await fetch("http://localhost:5000/run_deploy", { method: "POST" });
        const result = await response.json();
        alert(result.message);
    } catch (error) {
        alert("Failed to launch virtual board. Is the server running?");
    }
});
