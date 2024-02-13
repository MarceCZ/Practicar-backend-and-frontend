import React, { useEffect } from 'react'
import { useNavigate } from "react-router-dom";

const MainPage = () => {

  const navigate = useNavigate()

  useEffect(() => {
    if(sessionStorage.getItem("USERNAME")==null){
      navigate("/")
      return
    }
  }, [])

  return (
    <div>
      <h1>Login Correcto</h1>
    </div>
  )
}

export default MainPage
