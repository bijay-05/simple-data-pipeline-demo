import { useState } from 'react'
import './App.css'
import Tableview from './routes/table.jsx'
import Form from './routes/form.jsx'
import { Routes, Route, Link, useHref } from 'react-router-dom'


function App() {
  return (
    <div>
      <Routes>
        <Route path='/' exact element={<Home />}></Route>
        <Route path="/form" element={<Form />}></Route>
        <Route path="/view" element={<Tableview />}></Route>
      </Routes>
    </div>
  )
}

export default App

function Home() {
  return (
    <>
      <h1>Intern Information Portal</h1>
      <div className="button">
        <a href="/form">
          <button type="button">
            Add new intern
          </button>
        </a>
        <a href="/view">
          <button>
            View Existing Records
          </button>
        </a>
        <a>
          <button>
            Edit Information
          </button>
        </a>      
        <p>
          copyright@2020
        </p>
      </div>
      <p className="read-the-docs">
        Click to learn more
      </p> 
    </>    
  )
}