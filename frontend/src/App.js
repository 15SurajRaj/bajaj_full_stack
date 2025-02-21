import React, { useState } from "react";
import InputForm from "./components/InputForm";
import ResponseDisplay from "./components/ResponseDisplay";
import "./styles.css";

const App = () => {
  const [response, setResponse] = useState(null);

  return (
    <div className="container">
      <h1>BFHL Challenge</h1>
      <InputForm setResponse={setResponse} />
      {response && <ResponseDisplay response={response} />}
    </div>
  );
};

export default App;
