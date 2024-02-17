import React, {useState} from 'react'
import { FaSearch } from "react-icons/fa";
import './Hamburger.css'

const Hamburger =() => {

    const [burger_class, setBurgerClass] = useState("burger-bar unclicked")
    const [menu_class, setMenuClass] = useState("menu hidden")
    const [isMenuClicked, setIsMenuClicked] = useState(false)

    //toggle clicks
    const updateMenu = () => {
        if(!isMenuClicked){
            setBurgerClass("burger-bar clicked")
            setMenuClass("menu visible")
        }
        else{
            setBurgerClass("burger-bar unclicked")
            setMenuClass("menu is hidden")
        }
        setIsMenuClicked(!isMenuClicked)
    }

  return (
    <div style ={{width: '100%', height: '100vh'}}>
        <nav>
            <div className = "burger-menu" onClick={updateMenu}>
                <div className ={burger_class}></div>
                <div className ={burger_class}></div>
                <div className ={burger_class}></div>
            </div>
        </nav>
        <div className={menu_class}></div>
        <div className="searchbar">
          
          <input type="searchbar"placeholder='Search For Item' required />
          <FaSearch className='searchIcon'/>
        </div>
    </div>
  )
}

export default Hamburger