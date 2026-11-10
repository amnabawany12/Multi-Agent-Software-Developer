const loadingMessages = [
    "Requirement Analyst is analyzing your request...",
    "Code Generator is creating Python code...",
    "Testing Engineer is preparing test cases...",
    "Code Reviewer is reviewing the implementation...",
    "Preparing your final development report..."
];

let loadingInterval = null;


async function startDevelopment() {

    const requirement = document
        .getElementById("requirement")
        .value
        .trim();

    const button = document.getElementById("generateBtn");

    const loading = document.getElementById("loading");

    const errorBox = document.getElementById("errorBox");

    const results = document.getElementById("resultsContent");

    if (!requirement) {

        alert("Please enter a software requirement first.");

        return;
    }

    button.disabled = true;

    button.textContent = "Generating...";

    loading.classList.remove("hidden");

    errorBox.classList.add("hidden");

    results.classList.add("hidden");

    document.getElementById("loadingText").textContent =
        loadingMessages[0];

    let messageIndex = 0;

    loadingInterval = setInterval(() => {

        messageIndex = (messageIndex + 1) % loadingMessages.length;

        document.getElementById("loadingText").textContent =
            loadingMessages[messageIndex];

    }, 7000);


    try {

        const response = await fetch("/api/develop", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                requirement: requirement
            })

        });


        const data = await response.json();

        if (!response.ok) {

            throw new Error(data.detail || "Something went wrong.");

        }


        document.getElementById("planOutput").textContent =
            data.plan;

        document.getElementById("codeOutput").textContent =
            data.code;

        document.getElementById("testsOutput").textContent =
            data.tests;

        document.getElementById("reviewOutput").textContent =
            data.review;

        document.getElementById("reportOutput").textContent =
            data.report;


        window.latestReport = data.report;

        results.classList.remove("hidden");

        document.getElementById("results").scrollIntoView({
            behavior: "smooth"
        });

    }

    catch (error) {

        errorBox.textContent = "Error: " + error.message;

        errorBox.classList.remove("hidden");

    }

    finally {

        clearInterval(loadingInterval);

        loading.classList.add("hidden");

        button.disabled = false;

        button.textContent = "Generate Software →";

    }

}


// Download development report

function downloadReport() {

    const report = window.latestReport;

    if (!report) {

        alert("No development report available.");

        return;

    }

    const blob = new Blob(
        [report],
        { type: "text/plain" }
    );

    const url = URL.createObjectURL(blob);

    const link = document.createElement("a");

    link.href = url;

    link.download = "Development_Report.txt";

    link.click();

    URL.revokeObjectURL(url);

}