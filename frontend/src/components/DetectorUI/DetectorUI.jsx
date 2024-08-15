import React from 'react';
import './DetectorUI.css';
import SearchBar from '../SearchBar/SearchBar';

const DetectorUI = () => {
    return (
        <div className="detector-ui">
            <div className="content">
                <SearchBar />
            </div>
        </div>
    );
};

export default DetectorUI;
