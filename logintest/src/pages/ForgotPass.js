import React from 'react'
import './LoginSignup.css'
import { FaUser, FaLock } from "react-icons/fa";

function ForgotPass() {
  return (
    <div className='background'>
    <div className = {"container"}>
        <form action="">
        <h1>Reset Password</h1>

        <div className="inputs">
            <input type="username"placeholder='Username'required />
            <FaUser className ='icon'/>
        </div>

        <div className="inputs">
          
                <input type="password"placeholder='Password' required />
                <FaLock className='icon'/>
        </div>
        <div className="inputs">
          
          <input type="password"placeholder='Re-enter Password' required />
          <FaLock className='icon'/>
        </div>

        <button className="login"  href="/"><a href="/" >Submit </a></button>

      </form>
    </div>
    </div>

  )
}

export default ForgotPass