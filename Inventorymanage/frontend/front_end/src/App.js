import react from 'react'
import { BrowserRouter as Router,Link,Route,Routes } from 'react-router-dom';
import NavBar from './components/NavBar';
import {ProductProvider} from './ProductContext'


function App() {
  return (
    <div>
      <Router>
        <ProductProvider>
        <NavBar/>
        </ProductProvider>
        
      </Router>
    </div>
  );
}

export default App;
