import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'collapsible-card',
  templateUrl: './collapsible-card.component.html',
  styleUrls: ['./collapsible-card.component.scss']
})
export class CollapsibleCardComponent implements OnInit {

  @Input() isOpen: boolean;
  @Input() wrappedElement: any;
  constructor() { }

  ngOnInit(): void {

  }

}
