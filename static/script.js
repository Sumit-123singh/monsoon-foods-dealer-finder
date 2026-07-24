// const searchInput = document.getElementById("searchInput");
// const searchBtn = document.getElementById("searchBtn");
// const locationBtn = document.getElementById("locationBtn");

// const dealerContainer = document.getElementById("dealerContainer");

// const loader = document.getElementById("loader");

// const emptyState = document.getElementById("emptyState");

// const errorBox = document.getElementById("errorBox");

// // ----------------------------
// // Utility Functions
// // ----------------------------

// function showLoader() {
//     loader.classList.remove("hidden");
// }

// function hideLoader() {
//     loader.classList.add("hidden");
// }

// function hideEmptyState() {
//     emptyState.style.display = "none";
// }

// function showEmptyState() {
//     emptyState.style.display = "block";
// }

// function clearError() {
//     errorBox.classList.add("hidden");
//     errorBox.innerHTML = "";
// }

// function showError(message) {

//     errorBox.classList.remove("hidden");

//     errorBox.innerHTML = `
//         <strong>Error</strong><br>
//         ${message}
//     `;
// }

// function clearResults() {

//     dealerContainer.innerHTML = "";
// }

// // ----------------------------
// // Search Dealer
// // ----------------------------

// async function searchDealer() {

//     clearResults();

//     clearError();

//     hideEmptyState();

//     const query = searchInput.value.trim();

//     if (query === "") {

//         showError("Please enter dealer name or pincode.");

//         showEmptyState();

//         return;
//     }

//     showLoader();

//     try {

//         const response = await fetch(

//             `/api/search?query=${encodeURIComponent(query)}`

//         );

//         if (!response.ok) {

//             throw new Error("Unable to fetch dealers.");
//         }

//         const dealers = await response.json();

//         hideLoader();

//         renderDealers(dealers);

//     }

//     catch (error) {

//         hideLoader();

//         showError(error.message);

//         showEmptyState();

//     }

// }

// // ----------------------------
// // Current Location
// // ----------------------------

// function findNearestDealers() {

//     clearResults();

//     clearError();

//     hideEmptyState();

//     if (!navigator.geolocation) {

//         showError(

//             "Geolocation is not supported by your browser."

//         );

//         return;

//     }

//     showLoader();

//     navigator.geolocation.getCurrentPosition(

//         async (position) => {

//             const lat = position.coords.latitude;

//             const lon = position.coords.longitude;

//             try {

//                 const response = await fetch(

//                     `/api/nearest?lat=${lat}&lon=${lon}`

//                 );

//                 if (!response.ok) {

//                     throw new Error(

//                         "Unable to fetch nearby dealers."

//                     );

//                 }

//                 const dealers = await response.json();

//                 hideLoader();

//                 renderDealers(dealers);

//             }

//             catch (error) {

//                 hideLoader();

//                 showError(error.message);

//             }

//         },

//         () => {

//             hideLoader();

//             showError(

//                 "Permission denied. Please allow location access."

//             );

//         }

//     );

// }

// // ----------------------------
// // Dealer Card
// // ----------------------------

// function dealerCard(dealer) {

//     const distance = dealer.distance
//         ? `${dealer.distance} km away`
//         : "Distance unavailable";

//     return `

//     <div class="dealer-card">

//         <div class="dealer-header">

//             <div>

//                 <div class="dealer-name">

//                     ${dealer.name}

//                 </div>

//             </div>

//             <div class="distance-badge">

//                 ${distance}

//             </div>

//         </div>

//         <div class="info">

//             <p>

//                 <i class="fa-solid fa-location-dot"></i>

//                 ${dealer.district}

//             </p>

//             <p>

//                 <i class="fa-solid fa-map-pin"></i>

//                 ${dealer.pincode}

//             </p>

//             <p>

//                 <i class="fa-solid fa-phone"></i>

//                 ${dealer.phone}

//             </p>

//         </div>

//         <div class="actions">

//             <a

//                 href="tel:${dealer.phone}"

//                 class="action-btn call">

//                 📞 Call

//             </a>

//             <a

//                 href="https://wa.me/91${dealer.phone}"

//                 target="_blank"

//                 class="action-btn whatsapp">

//                 💬 WhatsApp

//             </a>

//             <a

//                 href="https://www.google.com/maps/dir/?api=1&destination=${dealer.latitude},${dealer.longitude}"

//                 target="_blank"

//                 class="action-btn direction">

//                 📍 Directions

//             </a>

//         </div>

//     </div>

//     `;
// }

// // ----------------------------
// // Render Dealers
// // ----------------------------

// function renderDealers(dealers) {

//     clearResults();

//     if (dealers.length === 0) {

//         showEmptyState();

//         return;
//     }

//     dealers.forEach((dealer) => {

//         dealerContainer.innerHTML += dealerCard(dealer);

//     });

// }

// // ----------------------------
// // Event Listeners
// // ----------------------------

// searchBtn.addEventListener(

//     "click",

//     searchDealer

// );

// locationBtn.addEventListener(

//     "click",

//     findNearestDealers

// );

// searchInput.addEventListener(

//     "keypress",

//     function (event) {

//         if (event.key === "Enter") {

//             searchDealer();

//         }

//     }

// );

// // ----------------------------
// // Page Ready
// // ----------------------------

// window.onload = () => {

//     console.log(

//         "Dealer Finder Loaded Successfully"

//     );

// };


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