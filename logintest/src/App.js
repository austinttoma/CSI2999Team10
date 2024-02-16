
import './App.css';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
//pages
import  LoginSignup  from './pages/LoginSignup';
import ForgotPass from './pages/ForgotPass';
import Register from './pages/Register';
import HomePage from './pages/HomePage';

function App() {
  return (
    <div className = "pageContainer" >
      <BrowserRouter>
      <Switch>
          
        <Route exact path="/">
         <LoginSignup/></Route>  
        <Route exact path="/forgotpass">
         <ForgotPass/></Route>
         <Route exact path="/register">
          <Register/></Route>
        
        <Route exact path="/home">
          <HomePage/></Route>  
        
      </Switch>
      </BrowserRouter>
      
    </div>
    
  );
}

export default App;
