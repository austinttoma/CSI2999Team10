import React from 'react'
import './LoginSignup.css'
import { FaUser, FaLock } from "react-icons/fa";

function LoginSignup()  {
  return (
    <div className='background'>
    <div className='container'>
        <form action="">
        <h1>Login</h1>

        <div className="inputs">
            <input type="username"placeholder='Username'required />
            <FaUser className ='icon'/>
        </div>

        <div className="inputs">
          
                <input type="password"placeholder='Password' required />
                <FaLock className='icon'/>
       
        </div>
        <div className="forgot">
            <p>Forgot Password?<a href="/forgotpass"> Click Here</a></p>
            
        </div>
        <button className="login" ><a href="/home" >Login</a></button>
        <div className="register">
            <p>Dont have an account?<a href="/register"> Register </a></p>
        </div>
      </form>
    </div>
    </div>
        
  );
};
export default LoginSignup;