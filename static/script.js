

console.log("JS Loaded");

document.getElementById("searchBtn").addEventListener("click", async () => {

    console.log("Button clicked");

    const query = document.getElementById("searchInput").value;

    console.log(query);

    const response = await fetch(`/api/search?query=${encodeURIComponent(query)}`);

    console.log(response.status);

    const data = await response.json();

    console.log(data);

    alert(JSON.stringify(data));
});