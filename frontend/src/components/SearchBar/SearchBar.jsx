import {React, useState} from 'react'
import Swal from "sweetalert2"
import axios from 'axios';
import "./SearchBar.css"

const SearchBar = () => {

    const [url,setUrl] = useState("")

    const handleChange = (e) => {
        setUrl(e.target.value);
    }

    const handleSubmission = async () => {
        Swal.showLoading();
        const res = await axios.post('http://localhost:5000/submit', { url });
        Swal.hideLoading();
        let isPhshing = res.data.response;
        console.log(isPhshing)
        if(isPhshing){
            Swal.fire({
                title:"Hurrahh!!",
                text:"The Link is Legitimate",
                icon:"success",
                confirmButtonText:"Close"
            })
        } else {
            Swal.fire({
                title:"Alass!!",
                text:"The Link is Suspicious",
                icon:"error",
                confirmButtonText:"Close"
            })
        }
    }
    return (
        <div className='search-box'>
            <h1 className='slogan'>Instantly Verify Legitimate Sites with AntiPhish AI</h1>
            <input 
                type="text" 
                value={url}
                onChange={handleChange}
                className='url-input' 
                placeholder='Enter the URL'
            />
            <button onClick = {handleSubmission} className="submit-button">Submit</button>
        </div>
    )
};

export default SearchBar;