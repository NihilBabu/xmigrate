import React from "react";
import "./App.css";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
// import BluePrint from './pages/BluePrint/BluePrint';
// import CreateWorkspace from './pages/CreateWorkspace/CreateWorkspace';
// import Dashboard from './pages/Dashboard/Dashboard';
import Home from "./pages/Home/Home";
import SignIn from "./pages/SignIn/SignIn";
import Project from "./pages/Project/Project";
import SignUp from "./pages/SignUp/SignUp";
import { ProtectedRoute } from "./services/Protected.route";

function App() {
  return (
    <div className="App h-100">
      <Router>
        <Switch>
          <Route exact path="/" component={SignIn} />
          <Route exact path="/signup" component={SignUp} />
          <ProtectedRoute path="/home" component={Home} />
          <ProtectedRoute path="/Project" component={Project} />
          <Route
            path="/error"
            component={() => {
              return (
                <div className="d-flex justify-content-center align-items-center h-100">
                  <h4>Sry For the Error!! Will fix it soon</h4>
                </div>
              );
            }}
          />
             <Route
            path="/401"
            component={() => {
              return (
                <div className="d-flex justify-content-center align-items-center h-100">
                <h2>401 !!!Unauthorized Access</h2>
              </div>
              )
            }}
          />
          <Route
            path="/404"
            component={() => {
              return (
                <div className="d-flex justify-content-center align-items-center h-100">
                <h2>404 !!!Server not Found</h2>
              </div>
              )
            }}
          />
                <Route
            path="/500"
            component={() => {
              return (
                <div className="d-flex justify-content-center align-items-center h-100">
                <h2>500 !!!Internal Server Error</h2>
              </div>
              )
            }}
          />
            <Route
            path="/400"
            component={() => {
              return (
                <div className="d-flex justify-content-center align-items-center h-100">
                <h2>400 !!!Request Error</h2>
              </div>
              )
            }}
          />
        </Switch>
      </Router>
    </div>
  );
}

export default App;
