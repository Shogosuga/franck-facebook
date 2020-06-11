import React from 'react';
import ReactDOM from 'react-dom';
import FacebookBtn from './compoenent/FacebookBtn';


class App extends React.Component {
    render() {
        return (
            <div>
                Try to login using Facebook API
            </div>
        );
    }
}

ReactDOM.render(<App />, document.getElementById('app'));
