async function convert() {
    const jp = document.getElementById("jp").value;
    const res = await fetch("http://localhost:5001/api/convert", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: jp, to: "formal" })
    });
    const data = await res.json();
    document.getElementById("kr").value = data.converted;
  }
