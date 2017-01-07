import React from 'react';
import {connect} from 'react-redux';

class CartItem extends React.Component {
    render() {
        const cartItem = this.props.cartItem;
        return (
            <div>
                cI
                <button>+</button>
                <span>{cartItem.get('quantity')}</span>
                <button>-</button>
            </div>

        )
    }
}

class Cart extends React.Component {
    render() {
        const cart = this.props.cart;
        return (
            <div>
                CART:
                {cart.map(
                    (cartItem, index) => <CartItem key={index} cartItem={cartItem} />
                )}
            </div>
        )
    }
}

export const ConnectedCart = connect(
    function mapStateToProps(state) {
        return {
            cart: state.get('cart'),
        }
    },
    function mapDispatchToProps(dispatch) {
        return {
            // selectVideo: videoSlug => dispatch(actions.selectVideo(videoSlug)),
            // selectLivestream: videoSlug => dispatch(actions.selectLivestream()),
            // switchToNextInPlaylist: () => dispatch(actions.switchToNextInPlaylist()),
        }
    }
)(Cart);