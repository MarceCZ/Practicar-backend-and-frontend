import { TextField,Box,Container, Alert,Button } from '@mui/material'
import React, { useEffect, useState } from 'react'
import CheckIcon from "@mui/icons-material/Check"
import { useNavigate } from 'react-router-dom'

const LoginPage = () => {
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    const [loginIncorrecto, setLoginIncorrecto] = useState(false)

    const navigate = useNavigate()

    const loginOnClick = async () => {

        const response = await fetch(`http://localhost:8000/proyectos/login?username=${username}&password=${password}`)
        const data = await response.json()

        if(data.msg === ""){
            sessionStorage.setItem("USERNAME", username)

            navigate("/main", {
                state : {
                    username : username
                }
            })
        }
        else{
            setLoginIncorrecto(true)
        }
    }

    useEffect(() =>{
        if(sessionStorage.getItem("USERNAME")!=null){
            navigate("/main")
            return
        }
    },[])

    return <Container
        maxWidth="sm">
        <Box
            component="form"
            noValidate
            autoComplete="off"
            sx={{ textAlign: "center" }}>
            <h1>Login</h1>
            <div>
                <TextField
                    required
                    label="Username"
                    margin="normal"
                    value = {username}
                    onChange = {(e) => {setUsername(e.target.value)}}
                />
            </div>
            <div>
                <TextField
                    required
                    type = "password"
                    label = "Password"
                    margin = "normal"
                    value = {password}
                    onChange = {(e) => {setPassword(e.target.value)}}/>
            </div>
            <div>
                <Button
                    variant="contained"
                    style = {{marginRight: "8px"}}
                    onClick={loginOnClick}>
                        Login
                </Button>
                <Button
                    variant = "contained">
                        Registro
                </Button>
            </div>
            {
                (() => {
                    if (loginIncorrecto) {
                        return <Alert 
                            icon={<CheckIcon fontSize="inherit" />} 
                            severity="error"
                            sx={ { mt : 2 } }>
                            Error en el login.
                        </Alert>
                    }
                })()
            }
        </Box>
    </Container>
}

export default LoginPage
