import React from 'react';
import {Link} from 'react-router-dom';
import '../App.css';

import autoData from '../jsons/automobiles.json';
import cryptoData from '../jsons/cryptocurrency.json';
import departmentData from '../jsons/departmentstore.json';
import entertainData from '../jsons/entertainment.json';
import etfData from '../jsons/etf.json';
import financeData from '../jsons/finance.json';
import homegoodData from '../jsons/homegoods.json';
import insuranceData from '../jsons/insurance.json';
import onlineData from '../jsons/onlineretail.json';
import gameData from '../jsons/videogames.json';
import wholesaleData from '../jsons/wholesale.json';

export default function Home() {

    return (
        <div className='App-container' >     
            <head className='App-header'>    
                <h1 className='App'>trendi</h1>
            </head>
            <body style={{display: 'flex'}}>
                <view className='container'>
                    <view className='App-watchlist-backing' />
                    <view className='Button-container'>
                        <Link to={{pathname: './StockData', state: {data: financeData}}} className='App-watchlist-item'>
                            <text className='App-watchlist-item-text'>FINANCE</text>
                        </Link>
                        <Link to={{pathname: './StockData', state: {data: autoData}}} className='App-watchlist-item'>
                            <text className='App-watchlist-item-text'>AUTO</text>
                        </Link>
                        <Link to={{pathname: './StockData', state: {data: homegoodData}}} className='App-watchlist-item'>
                            <text className='App-watchlist-item-text'>HOMEGOODS</text>
                        </Link>
                        <Link to={{pathname: './StockData', state: {data: wholesaleData}}} className='App-watchlist-item'>
                            <text className='App-watchlist-item-text'>GROCERY & WHOLESALE</text>
                        </Link>
                        <Link to={{pathname: './StockData', state: {data: gameData}}} className='App-watchlist-item'>
                            <text className='App-watchlist-item-text'>VIDEO GAMES</text>
                        </Link>
                        <Link to={{pathname: './StockData', state: {data: entertainData}}} className='App-watchlist-item'>
                            <text className='App-watchlist-item-text'>ENTERTAINMENT</text>
                        </Link>
                        <Link to={{pathname: './StockData', state: {data: departmentData}}} className='App-watchlist-item'>
                            <text className='App-watchlist-item-text'>DEPARTMENT/CLOTHING STORE</text>
                        </Link>
                        <Link to={{pathname: './StockData', state: {data: onlineData}}} className='App-watchlist-item'>
                            <text className='App-watchlist-item-text'>ONLINE SHOPPING</text>
                        </Link>
                        <Link to={{pathname: './StockData', state: {data: insuranceData}}} className='App-watchlist-item'>
                            <text className='App-watchlist-item-text'>INSURANCE</text>
                        </Link>
                        <Link to={{pathname: './StockData', state: {data: etfData}}} className='App-watchlist-item'>
                            <text className='App-watchlist-item-text'>ETF</text>
                        </Link>
                        <Link to={{pathname: './StockData', state: {data: cryptoData}}} className='App-watchlist-item'>
                            <text className='App-watchlist-item-text'>CRYPTOCURRENCY</text>
                        </Link>
                    </view>
                </view>
            </body>
        </div>
    )
    
}