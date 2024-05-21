/** @odoo-module */

import { usePos } from "@point_of_sale/app/store/pos_hook";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { Component } from "@odoo/owl";

export class ClearButton extends Component {
    static template = "pos_usecase.ClearButton";

    setup() {
        this.pos = usePos();
    }
    click() {
       console.log(this.pos)
       
       const selectedLine = this.pos.get_order().get_selected_orderline();
       this.pos.get_order().removeOrderline(selectedLine);
    }
}

ProductScreen.addControlButton({
    component: ClearButton,
    condition: function () {
        return true;
    },
});
