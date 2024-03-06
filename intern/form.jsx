import axios from 'axios';
import { useState } from 'react';


export default function Form() {
    const [id, setId] = useState("")
    const [name, setName] = useState("")
    const [address, setAddress] = useState("")
    const [dob, setDob] = useState("")
    const [status, setStatus] = useState("")


    const handleSubmit = async (e) => {
        e.preventDefault()
        try {
            await axios.post('http://localhost:3000/internmembers', {"id":id,"name":name,"address":address,"dob":dob,"status":status});
            alert('Intern added successfully!');
            // Reset values
            setId("")
            setName("")
            setAddress("")
            setDob("")
            setStatus("")
          } catch (error) {
            console.error('Failed to add intern member:', error);
            alert('Failed to add intern.');
          }

    }

    return (
        <>
        <h1>Create New Intern Record</h1>
        <div>
            <form>
                <input placeholder='Enter ID' onChange={(e) => {setId(e.target.value)}} value={id}></input>
                <input placeholder='Enter name' onChange={(e) => {setName(e.target.value)}} value={name}></input>
                <input placeholder='Enter address' onChange={(e) => {setAddress(e.target.value)}} value={address}></input>
                <input placeholder='Enter Date of birth' onChange={(e) => {setDob(e.target.value)}} value={dob}></input>
                <input placeholder='Enter Y or N' onChange={(e) => {setStatus(e.target.value)}} value={status}></input>
                <button type="submit" onClick={(e) => {handleSubmit}}>Add member</button>
            </form>
        </div>
        </>
    )
}