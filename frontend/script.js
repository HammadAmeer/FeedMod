const form = document.getElementById("feedback-form");
const input = document.getElementById("feedback-input");
const list = document.getElementById("feedback-list");

// Submit feedback via AJAX
form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const message = input.value.trim();
  if (message === "") return;

  try {
    await fetch("http://127.0.0.1:8000/submit-feedback", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message }),
    });
    input.value = "";
  } catch (err) {
    console.error("Failed to submit feedback", err);
  }
});

// Poll feedback list every 2 seconds
async function loadFeedback() {
  try {
    const res = await fetch("http://127.0.0.1:8000/get-feedback");
    const data = await res.json();

    // Clear old list
    list.innerHTML = "";

    // Render all feedback
    data.feedback.forEach((msg) => {
      const li = document.createElement("li");
      li.textContent = msg;
      list.appendChild(li);
    });
  } catch (err) {
    console.error("Failed to fetch feedback", err);
  }
}

setInterval(loadFeedback, 2000); // Auto-refresh
loadFeedback(); // Load once initially
