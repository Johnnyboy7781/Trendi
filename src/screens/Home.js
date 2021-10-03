import React from 'react';
import {Link} from 'react-router-dom';
import '../App.css';

import indusData from '../jsons/industrials.json';
import healthData from '../jsons/healthcare.json';
import infotechData from '../jsons/informationtechnology.json';
import commservData from '../jsons/communicationservices.json';
import constapData from '../jsons/consumerstaples.json';
import consdisData from '../jsons/consumerdiscretionary.json';
import utilitiesData from '../jsons/utilities.json';
import financialsData from '../jsons/financials.json';
import materialsData from '../jsons/materials.json';
import realestData from '../jsons/realestate.json';
import evergyData from '../jsons/energy.json';

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
                        <Link to={{pathname: './StockData', state: {data: indusData}}} className='App-watchlist-item'>
                            <text className='App-watchlist-item-text'>INDUSTRIALS</text>
                        </Link>
                        <Link to={{pathname: './StockData', state: {data: healthData}}} className='App-watchlist-item'>
                            <text className='App-watchlist-item-text'>HEALTHCARE</text>
                        </Link>
                        <Link to={{pathname: './StockData', state: {data: evergyData}}} className='App-watchlist-item'>
                            <text className='App-watchlist-item-text'>ENERGY</text>
                        </Link>
                        <Link to={{pathname: './StockData', state: {data: realestData}}} className='App-watchlist-item'>
                            <text className='App-watchlist-item-text'>REAL ESTATE</text>
                        </Link>
                        <Link to={{pathname: './StockData', state: {data: materialsData}}} className='App-watchlist-item'>
                            <text className='App-watchlist-item-text'>MATERIALS</text>
                        </Link>
                        <Link to={{pathname: './StockData', state: {data: financialsData}}} className='App-watchlist-item'>
                            <text className='App-watchlist-item-text'>FINANCIALS</text>
                        </Link>
                        <Link to={{pathname: './StockData', state: {data: utilitiesData}}} className='App-watchlist-item'>
                            <text className='App-watchlist-item-text'>UTILITIES</text>
                        </Link>
                        <Link to={{pathname: './StockData', state: {data: consdisData}}} className='App-watchlist-item'>
                            <text className='App-watchlist-item-text'>CONSUMER DISCRETIONARY</text>
                        </Link>
                        <Link to={{pathname: './StockData', state: {data: constapData}}} className='App-watchlist-item'>
                            <text className='App-watchlist-item-text'>CONSUMER STAPLES</text>
                        </Link>
                        <Link to={{pathname: './StockData', state: {data: commservData}}} className='App-watchlist-item'>
                            <text className='App-watchlist-item-text'>COMMUNICATIONS SERVICE</text>
                        </Link>
                        <Link to={{pathname: './StockData', state: {data: infotechData}}} className='App-watchlist-item'>
                            <text className='App-watchlist-item-text'>INFORMATION TECHNOLOGY</text>
                        </Link>
                    </view>
                </view>
            </body>
        </div>
    )
    
}