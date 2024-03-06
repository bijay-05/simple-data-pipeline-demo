import axios from "axios"
import { useEffect, useState } from "react"

export default function Tableview() {
    const [data, setData] = useState(null)
    const [loader, setLoader] = useState(false)
    const [error, setError] = useState('')
    
    // useEffect runs after rendering below markup
    useEffect(() => {
        async function loadInterns() {
            setLoader(true)
            setError('')
            try {
                const list = await axios.get('http://localhost:3000/interns')
                setData(list.data)
            } catch (e) {
                console.log(e)
                setError('Error fetching records !!!')
            } finally {
                setLoader(false)
            }
        }
        loadInterns()
    }, [])
    return (<>
        <h1>Interns Information Table</h1>
        {loader &&
            <h2>You spin me right round</h2>
        }
        <div style={{ display: 'flex' }}>
            {data && data.map(item => {
                return <InternItemComponent key={`intern` + item.id} {...item} />
                // react uses key attribute to identify an element of same type among its siblings
                // during re-renders
            })}
        </div>
        {error}
    </>
    )
}

const InternItemComponent = (props) => {
    const {id, name, address, dob, status } = props
    return <div style={{ flex: 1, background: 'white', border: '1px solid grey', borderRadius: '10px', color: 'black', margin: '10px' }}>
        <h4>InternID: {id}</h4>
        <h4>Name: {name}</h4>
        <h4>Address: {address}</h4>  
        <h4>Date Of Birth: {dob}</h4>
        <h4>Selection Status: {status}</h4>
    </div>
}