import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { InsertCategoryFormComponent } from './insert-category-form.component';

describe('InsertCategoryFormComponent', () => {
  let component: InsertCategoryFormComponent;
  let fixture: ComponentFixture<InsertCategoryFormComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ InsertCategoryFormComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(InsertCategoryFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
