import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Generate from './pages/Generate';
import About from './pages/About';


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Generate />} />
        <Route path='/about' element={<About />} />
      </Routes>
    </Router>
  );
}

export default App;
