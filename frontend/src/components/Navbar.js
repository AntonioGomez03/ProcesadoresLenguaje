import React, { useState } from 'react';
import { NavLink } from 'react-router-dom';

const Navbar = () => {
    return (
        <nav className='navbar'>
            <ul>
                <li>
                    <NavLink to='/' end>Generate</NavLink>
                </li>
                <li>
                    <NavLink to='/manual'>Manual</NavLink>
                </li>
                <li>
                    <NavLink to='/objetives'>Objetives</NavLink>
                </li>
            </ul>
        </nav>
    );
}

export default Navbar;