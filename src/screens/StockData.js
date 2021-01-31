import React from 'react';
import '../StockData.css';
import '../App.css';

export default class StockData extends React.Component {

    render() {

        const data = this.props.location.state;

        return (
            <div className='App-container'>
                <head className='App-header'>    
                    <h1 className='App'>trendi</h1>
                </head>
                <body className='Data-container' >

                    { /* Left side view */ }
                    <view className='Data-stocks1'>
                        <view className='Stock-data'>
                            <view className='Stock-data-sq1'>
                                <text style={{fontSize: 45, color: data.data.stocks["Recent Trajectories"][0] === 'Positive' ? 'green' : data.data.stocks["Recent Trajectories"][0] === 'Negative' ? 'red' : 'black'}}>{data.data.stocks['Stock Names'][0]}</text>
                            </view>
                            <view className='Stock-data-sq2'>
                                <view className='sq2-1'><text className='sq2-1-text'>Stability coefficient:</text></view>
                                <view className='sq2-2'>
                                    <view className='sq2-2-container'><text className='sq2-2-text'>{Number.parseFloat(data.data.stocks["Stability Coefficients (highs)"][0]).toFixed(1)}</text></view>
                                    <view className='sq2-2-container'><text className='sq2-2-text'>{Number.parseFloat(data.data.stocks["Stability Coefficients (at close)"][0]).toFixed(1)}</text></view>
                                </view>
                                <view className='sq2-3'>
                                    <view className='sq2-3-container'><text className='sq2-3-text'>(high)</text></view>
                                    <view className='sq2-3-container'><text className='sq2-3-text'>(close)</text></view>
                                </view>
                            </view>
                            <view className='Stock-data-sq3'>
                                <view className='sq3-container'><text className='sq3-text'>Trajectory:</text></view>
                                <view className='sq3-container'><text style={{fontSize: 25, color: data.data.stocks["Recent Trajectories"][0] === 'Positive' ? 'green' : data.data.stocks["Recent Trajectories"][0] === 'Negative' ? 'red' : 'black'}}>{data.data.stocks["Recent Trajectories"][0]}</text></view>
                            </view>
                        </view>
                        <view className='Stock-data'>
                            <view className='Stock-data-sq1'>
                                <text style={{fontSize: 45, color: data.data.stocks["Recent Trajectories"][1] === 'Positive' ? 'green' : data.data.stocks["Recent Trajectories"][1] === 'Negative' ? 'red' : 'black'}}>{data.data.stocks['Stock Names'][1]}</text>
                            </view>
                            <view className='Stock-data-sq2'>
                                <view className='sq2-1'><text className='sq2-1-text'>Stability coefficient:</text></view>
                                <view className='sq2-2'>
                                    <view className='sq2-2-container'><text className='sq2-2-text'>{Number.parseFloat(data.data.stocks["Stability Coefficients (highs)"][1]).toFixed(1)}</text></view>
                                    <view className='sq2-2-container'><text className='sq2-2-text'>{Number.parseFloat(data.data.stocks["Stability Coefficients (at close)"][1]).toFixed(1)}</text></view>
                                </view>
                                <view className='sq2-3'>
                                    <view className='sq2-3-container'><text className='sq2-3-text'>(high)</text></view>
                                    <view className='sq2-3-container'><text className='sq2-3-text'>(close)</text></view>
                                </view>
                            </view>
                            <view className='Stock-data-sq3'>
                                <view className='sq3-container'><text className='sq3-text'>Trajectory:</text></view>
                                <view className='sq3-container'><text style={{fontSize: 25, color: data.data.stocks["Recent Trajectories"][1] === 'Positive' ? 'green' : data.data.stocks["Recent Trajectories"][1] === 'Negative' ? 'red' : 'black'}}>{data.data.stocks["Recent Trajectories"][1]}</text></view>
                            </view>
                        </view>
                        <view className='Stock-data'>
                            <view className='Stock-data-sq1'>
                                <text style={{fontSize: 45, color: data.data.stocks["Recent Trajectories"][2] === 'Positive' ? 'green' : data.data.stocks["Recent Trajectories"][2] === 'Negative' ? 'red' : 'black'}}>{data.data.stocks['Stock Names'][2]}</text>
                            </view>
                            <view className='Stock-data-sq2'>
                                <view className='sq2-1'><text className='sq2-1-text'>Stability coefficient:</text></view>
                                <view className='sq2-2'>
                                    <view className='sq2-2-container'><text className='sq2-2-text'>{Number.parseFloat(data.data.stocks["Stability Coefficients (highs)"][2]).toFixed(1)}</text></view>
                                    <view className='sq2-2-container'><text className='sq2-2-text'>{Number.parseFloat(data.data.stocks["Stability Coefficients (at close)"][2]).toFixed(1)}</text></view>
                                </view>
                                <view className='sq2-3'>
                                    <view className='sq2-3-container'><text className='sq2-3-text'>(high)</text></view>
                                    <view className='sq2-3-container'><text className='sq2-3-text'>(close)</text></view>
                                </view>
                            </view>
                            <view className='Stock-data-sq3'>
                                <view className='sq3-container'><text className='sq3-text'>Trajectory:</text></view>
                                <view className='sq3-container'><text style={{fontSize: 25, color: data.data.stocks["Recent Trajectories"][2] === 'Positive' ? 'green' : data.data.stocks["Recent Trajectories"][2] === 'Negative' ? 'red' : 'black'}}>{data.data.stocks["Recent Trajectories"][2]}</text></view>
                            </view>
                        </view>
                        <view className='Stock-data'>
                            <view className='Stock-data-sq1'>
                                <text style={{fontSize: 45, color: data.data.stocks["Recent Trajectories"][3] === 'Positive' ? 'green' : data.data.stocks["Recent Trajectories"][3] === 'Negative' ? 'red' : 'black'}}>{data.data.stocks['Stock Names'][3]}</text>
                            </view>
                            <view className='Stock-data-sq2'>
                                <view className='sq2-1'><text className='sq2-1-text'>Stability coefficient:</text></view>
                                <view className='sq2-2'>
                                    <view className='sq2-2-container'><text className='sq2-2-text'>{Number.parseFloat(data.data.stocks["Stability Coefficients (highs)"][3]).toFixed(1)}</text></view>
                                    <view className='sq2-2-container'><text className='sq2-2-text'>{Number.parseFloat(data.data.stocks["Stability Coefficients (at close)"][3]).toFixed(1)}</text></view>
                                </view>
                                <view className='sq2-3'>
                                    <view className='sq2-3-container'><text className='sq2-3-text'>(high)</text></view>
                                    <view className='sq2-3-container'><text className='sq2-3-text'>(close)</text></view>
                                </view>
                            </view>
                            <view className='Stock-data-sq3'>
                                <view className='sq3-container'><text className='sq3-text'>Trajectory:</text></view>
                                <view className='sq3-container'><text style={{fontSize: 25, color: data.data.stocks["Recent Trajectories"][3] === 'Positive' ? 'green' : data.data.stocks["Recent Trajectories"][3] === 'Negative' ? 'red' : 'black'}}>{data.data.stocks["Recent Trajectories"][3]}</text></view>
                            </view>
                        </view>
                        <view className='Stock-data'>
                            <view className='Stock-data-sq1'>
                                <text style={{fontSize: 45, color: data.data.stocks["Recent Trajectories"][4] === 'Positive' ? 'green' : data.data.stocks["Recent Trajectories"][4] === 'Negative' ? 'red' : 'black'}}>{data.data.stocks['Stock Names'][4]}</text>
                            </view>
                            <view className='Stock-data-sq2'>
                                <view className='sq2-1'><text className='sq2-1-text'>Stability coefficient:</text></view>
                                <view className='sq2-2'>
                                    <view className='sq2-2-container'><text className='sq2-2-text'>{Number.parseFloat(data.data.stocks["Stability Coefficients (highs)"][4]).toFixed(1)}</text></view>
                                    <view className='sq2-2-container'><text className='sq2-2-text'>{Number.parseFloat(data.data.stocks["Stability Coefficients (at close)"][4]).toFixed(1)}</text></view>
                                </view>
                                <view className='sq2-3'>
                                    <view className='sq2-3-container'><text className='sq2-3-text'>(high)</text></view>
                                    <view className='sq2-3-container'><text className='sq2-3-text'>(close)</text></view>
                                </view>
                            </view>
                            <view className='Stock-data-sq3'>
                                <view className='sq3-container'><text className='sq3-text'>Trajectory:</text></view>
                                <view className='sq3-container'><text style={{fontSize: 25, color: data.data.stocks["Recent Trajectories"][4] === 'Positive' ? 'green' : data.data.stocks["Recent Trajectories"][4] === 'Negative' ? 'red' : 'black'}}>{data.data.stocks["Recent Trajectories"][4]}</text></view>
                            </view>
                        </view>
                        <view className='Stock-data-last'>
                            <view className='Stock-data-sq1'>
                                <text style={{fontSize: 45, color: data.data.stocks["Recent Trajectories"][5] === 'Positive' ? 'green' : data.data.stocks["Recent Trajectories"][5] === 'Negative' ? 'red' : 'black'}}>{data.data.stocks['Stock Names'][5]}</text>
                            </view>
                            <view className='Stock-data-sq2'>
                                <view className='sq2-1'><text className='sq2-1-text'>Stability coefficient:</text></view>
                                <view className='sq2-2'>
                                    <view className='sq2-2-container'><text className='sq2-2-text'>{Number.parseFloat(data.data.stocks["Stability Coefficients (highs)"][5]).toFixed(1)}</text></view>
                                    <view className='sq2-2-container'><text className='sq2-2-text'>{Number.parseFloat(data.data.stocks["Stability Coefficients (at close)"][5]).toFixed(1)}</text></view>
                                </view>
                                <view className='sq2-3'>
                                    <view className='sq2-3-container'><text className='sq2-3-text'>(high)</text></view>
                                    <view className='sq2-3-container'><text className='sq2-3-text'>(close)</text></view>
                                </view>
                            </view>
                            <view className='Stock-data-sq3'>
                                <view className='sq3-container'><text className='sq3-text'>Trajectory:</text></view>
                                <view className='sq3-container'><text style={{fontSize: 25, color: data.data.stocks["Recent Trajectories"][5] === 'Positive' ? 'green' : data.data.stocks["Recent Trajectories"][5] === 'Negative' ? 'red' : 'black'}}>{data.data.stocks["Recent Trajectories"][5]}</text></view>
                            </view>
                        </view>
                    </view>

                    { /* Right side view */ }
                    <view className='Data-stocks2'>
                        <view className='stocks2-1'>
                            <text className='stocks2-1-text'>Sector: {data.data.stocks["Sector"]}</text>
                        </view>
                        <view className='stocks2-2'>
                            <text className='stocks2-2-text'>{data.data.stocks["Sector Summary"]}</text>
                        </view>
                        <view className='stocks2-3'>
                            <view className='stocks2-3-1'><text className='stocks2-3-1-text'>Market insights: </text></view>
                            <view>
                                <view className='stocks2_1'><text className='stocks_2-1-text'>Avg Stability Coef:</text></view>
                                <view className='stocks2_2'>
                                    <view className='stocks_2-2-container'><text className='stocks_2-2-text'>{Number.parseFloat(data.data.stocks["Avg Stab. Coefficient (highs)"]).toFixed(1)}</text></view>
                                    <view className='stocks_2-2-container'><text className='stocks_2-2-text'>{Number.parseFloat(data.data.stocks["Avg Stab. Coefficient (at close)"]).toFixed(1)}</text></view>
                                </view>
                                <view className='stocks2_3'>
                                    <view className='stocks_2-3-container'><text className='stocks_2-3-text'>(high)</text></view>
                                    <view className='stocks_2-3-container'><text className='stocks_2-3-text'>(close)</text></view>
                                </view>
                            </view>
                        </view>
                        <view className='stocks2-4'>
                        <view>
                                <view className='stocks2_1'><text className='stocks_2-1-text'>Avg Up Market:</text></view>
                                <view className='stocks2_2'>
                                    <view className='stocks_2-2-container'><text className='stocks_2-2-text'>{Number.parseFloat(data.data.stocks["Avg Up Market Length (days)"]).toFixed(0)}</text></view>
                                    <view className='stocks_2-2-container'><text className='stocks_2-2-text'>{Number.parseFloat(data.data.stocks["Avg Up Market Return (%)"]).toFixed(2)}</text></view>
                                </view>
                                <view className='stocks2_3'>
                                    <view className='stocks_2-3-container'><text className='stocks_2-3-text'>Length (d)</text></view>
                                    <view className='stocks_2-3-container'><text className='stocks_2-3-text'>Return (%)</text></view>
                                </view>
                            </view>
                            <view>
                                <view className='stocks2_1'><text className='stocks_2-1-text'>Avg Down Market:</text></view>
                                <view className='stocks2_2'>
                                    <view className='stocks_2-2-container'><text className='stocks_2-2-text'>{Number.parseFloat(data.data.stocks["Avg Down Market Length (days)"]).toFixed(0)}</text></view>
                                    <view className='stocks_2-2-container'><text className='stocks_2-2-text'>{Number.parseFloat(data.data.stocks["Avg Down Market Return (%)"]).toFixed(2)}</text></view>
                                </view>
                                <view className='stocks2_3'>
                                    <view className='stocks_2-3-container'><text className='stocks_2-3-text'>Length (d)</text></view>
                                    <view className='stocks_2-3-container'><text className='stocks_2-3-text'>Return (%)</text></view>
                                </view>
                            </view>
                        </view>
                    </view>
                </body>
            </div>
        )
    }
}