import React from 'react'
import './LoginSignup.css'
import { FaUser, FaLock } from "react-icons/fa";
import { MdEmail } from "react-icons/md";



function Register() {
  return (
    <div className='background'>
    <div className = {"container"}>
    <form action="">
    <h1>Register</h1>

    <div className="inputs">
        <input type="username"placeholder='Username'required />
        <FaUser className ='icon'/>
    </div>
    <div className="inputs">
        <input type="email"placeholder='E-mail'required />
        <MdEmail className ='icon'/>
    </div>

    <div className="inputs">
      
            <input type="password"placeholder='Password' required />
            <FaLock className='icon'/>
    </div>
    <div className="inputs">
      
      <input type="password"placeholder='Confirm Password' required />
      <FaLock className='icon'/>
    </div>

    <button className="login"  href="/"><a href="/" >Submit </a></button>

  </form>
</div>
</div>
  )
}

export default Register