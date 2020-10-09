import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { InsertPersonFormComponent } from './insert-person-form.component';

describe('InsertPersonFormComponent', () => {
  let component: InsertPersonFormComponent;
  let fixture: ComponentFixture<InsertPersonFormComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ InsertPersonFormComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(InsertPersonFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
