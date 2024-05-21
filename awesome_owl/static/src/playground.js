/** @odoo-module **/

import { Component, markup, useState } from "@odoo/owl";
import { Counter } from "./counter/counter"
import { Card } from "./card/card"
import { TodoList } from "./todo/todo_list";

export class Playground extends Component {
    static template = "awesome_owl.playground";
    static components = { Counter, Card, TodoList };

    setup() {
        this.counter = useState({ value: 0 });
        this.string1 = "<div>some text 1</div>";
        this.string2 = markup("<div>some text 2</div>");
    }

    incrementSum(){
        this.counter.value++;
    }
}
