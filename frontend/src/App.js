import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Generate from './pages/Generate';
import Manual from './pages/Manual';
import Objetives from './pages/Objetives';


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Generate />} />
        <Route path='/manual' element={<Manual />} />
        <Route path='/objetives' element={<Objetives />} />
      </Routes>
    </Router>
  );
}

export default App;
