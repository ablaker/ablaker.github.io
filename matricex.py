A=rand(n,p):
B=rand(p,m):
C=zeros(n,m):
for i=1:n
  for j=1:m
     C(i,j)=0.0;
     for k=1:p
        C(i,j) = C(i,j)+A(i,k)*B(k,j);
     end 
   end 
end