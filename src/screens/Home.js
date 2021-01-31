import React from 'react';
import {Link} from 'react-router-dom';
import '../App.css';

export default function Home() {
    return (
        <div>     
            <div className='App-header'>    
                <h1 className='App'>trendi</h1>
            </div>
            <div style={{flex: 1, textAlign: 'center', top: 10}}>
                <button className="Button">               
                  <Link to='/StockData'>Stock</Link>
                </button>
                <button className="Button">               
                  <Link to='/StockData'>Stock</Link>
                </button>
                <button className="Button">               
                  <Link to='/StockData'>Stock</Link>
                </button>
                <button className="Button">               
                  <Link to='/StockData'>Stock</Link>
                </button>
            </div>
        </div>
    )
}