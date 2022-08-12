import './App.css';
import Nav from './components/Nav';
import Menu from './components/Menu';
import Movies from './admin/movies';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <Nav />
      <div className="container-fluid">
        <div className="row">
          <Menu />

          <main className="col-md-9 ms-sm-auto col-lg-10 px-md-4">
            <BrowserRouter>
              <Routes>
                <Route path="/admin/movies" element={<Movies />} />
              </Routes>

            </BrowserRouter>
          </main>
        </div>
      </div>
    </div>

  );
}

export default App;
