document.getElementById("predictionForm").addEventListener("submit", async function (e) {
    e.preventDefault();
  
    const age = document.getElementById("age").value;
    const sex = document.getElementById("sex").value;
    const bmi = document.getElementById("bmi").value;
    const children = document.getElementById("children").value;
    const smoker = document.getElementById("smoker").value;
    const region = document.getElementById("region").value;
  
    const inputData = {
      age: parseInt(age),
      sex: sex,
      bmi: parseFloat(bmi),
      children: parseInt(children),
      smoker: smoker,
      region: region
    };
  
    try {
      const response = await fetch("http://localhost:8000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(inputData)
      });
  
      if (response.ok) {
        const result = await response.json();
        document.getElementById("result").innerText = `Predicted Charges: $${result.predicted_charges}`;
      } else {
        document.getElementById("result").innerText = "Error: Unable to fetch prediction. Please try again.";
      }
    } catch (error) {
      document.getElementById("result").innerText = "Error: Unable to connect to the server.";
    }
  });  