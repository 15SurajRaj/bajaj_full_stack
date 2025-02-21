import React, { useState } from "react";

const InputForm = ({ setResponse }) => {
  const [inputData, setInputData] = useState("");
  const BACKEND_URL = process.env.REACT_APP_BACKEND_URL || "/api";

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch(`${BACKEND_URL}/bfhl`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ data: JSON.parse(inputData) }),
      });
      const result = await response.json();
      setResponse(result);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <textarea
        value={inputData}
        onChange={(e) => setInputData(e.target.value)}
        placeholder='Enter JSON like {"data": ["A", "1", "B"]}'
      />
      <button type="submit">Submit</button>
    </form>
  );
};

export default InputForm;
