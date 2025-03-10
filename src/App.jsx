import './App.css'
import { Route, BrowserRouter as Router, Routes } from 'react-router-dom';
import Dashboard from './assets/components/dashboard/dashboard';
import Analytics from './assets/components/analytics/analytics';
import AIChat from './assets/components/aichat/aichat';

function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route path='/dashboard/' element={<Dashboard />} />
          <Route path='/analytics/' element={<Analytics />} />
          <Route path='/aichat/' element={<AIChat />} />
        </Routes>
      </Router>
    </>
  )
}

export default App