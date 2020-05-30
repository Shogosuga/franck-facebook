import React from 'react';
import ReactDOM from 'react-dom';
import FacebookBtn from './compoenent/FacebookBtn';


class App extends React.Component {
    render() {
        return (
            <div>
                My Flask React App!
                
            </div>
        );
    }
}

ReactDOM.render(<App />, document.getElementById('app'));
