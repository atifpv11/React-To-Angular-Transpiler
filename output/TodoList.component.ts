import { Component } from '@angular/core';

@Component({
  selector: 'app-todolist',
  templateUrl: './TodoList.component.html',
})
export class TodoListComponent {
  todos: string[] = ['Learn React', 'Build a transpiler'];
  newTodo: string = '';

  addTodo() {
    if (this.newTodo.trim()) {
          this.todos.push(this.newTodo);
          this.newTodo = '';
        }
  }
}