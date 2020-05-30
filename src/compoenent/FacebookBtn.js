import React, { Component } from 'react';
import FacebookLogin from 'react-facebook-login';


class FacebookBtn extends Component {
    constructor(props) {
        super(props);
        this.componentClicked = this.componentClicked.bind(this);
        this.responseFacebook = this.responseFacebook.bind(this);
    };

    componentClicked() {
        console.log('click!')
    }

    responseFacebook(response) {
        console.log(response);
    };

    render() {
        return (
            <FacebookLogin 
                appID="709688982856249"
                autoLoad={true}
                fields="name,email,picture"
                onClick={this.componentClicked}
                callback={this.responseFacebook}
            />
        )
    };
};


export default FacebookBtn;