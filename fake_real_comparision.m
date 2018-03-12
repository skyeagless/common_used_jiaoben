function[red_img]=fake_real_comparision(real,fake,minred,maxred)
real_gray=rgb2gray(real);
fake_gray=rgb2gray(fake);
reduce_img=imsubtract(real_gray,fake_gray);
[m,n]=size(reduce_img);
I=double(reduce_img);
L=255;
t=L/(maxred-minred);
for i=1:m
    for j=1:n
        if I(i,j)<=minred
            R(i,j)=0;
            G(i,j)=0;
            B(i,j)=0;
        elseif I(i,j)<=maxred
            R(i,j)=t*I(i,j)-t*minred;
            G(i,j)=0;
            B(i,j)=0;
        elseif I(i,j)<=L
            R(i,j)=L;
            G(i,j)=0;
            B(i,j)=0;
        end
    end
end

for i=1:m
    for j=1:n
        rgbim(i,j,1)=R(i,j);
        rgbim(i,j,2)=G(i,j);
        rgbim(i,j,3)=B(i,j);
    end
end
red_img=rgbim/256;


        
        
                