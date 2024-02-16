import React from 'react'
import './HomePage.css'
import { FaMagnifyingGlass } from "react-icons/fa6";

function HomePage (){
  return (
    <div className="homeContainer">
      <div className='head'>
        
        <div className="inputs">
          
          <input type="search"placeholder='Search for item' required />
          <FaMagnifyingGlass className='icon'/> </div>
      </div>
    </div>
  );
};

export default HomePage